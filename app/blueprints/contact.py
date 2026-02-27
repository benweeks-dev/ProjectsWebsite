from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from flask_wtf import FlaskForm
from flask_mail import Message
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app import db, mail
from app.models import ContactMessage

contact_bp = Blueprint('contact', __name__)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[Length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')


@contact_bp.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()

        recipient = current_app.config.get('MAIL_RECIPIENT')
        if recipient:
            try:
                email_subject = f"Portfolio Contact: {form.subject.data or '(no subject)'}"
                body = (
                    f"Name: {form.name.data}\n"
                    f"Email: {form.email.data}\n"
                    f"Subject: {form.subject.data}\n\n"
                    f"Message:\n{form.message.data}"
                )
                msg = Message(
                    subject=email_subject,
                    sender=current_app.config['MAIL_USERNAME'],
                    recipients=[recipient],
                    body=body,
                    reply_to=form.email.data
                )
                mail.send(msg)
            except Exception as e:
                print(f"Mail error: {e}")
                pass  # Message already saved to DB; don't fail the request over email

        flash('Your message has been sent! I will get back to you soon.', 'success')
        return redirect(url_for('contact.contact'))
    return render_template('contact.html', form=form)
