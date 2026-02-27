import threading
import resend
from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app import db
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

        api_key = current_app.config.get('RESEND_API_KEY')
        recipient = current_app.config.get('MAIL_RECIPIENT')
        if api_key and recipient:
            email_subject = f"Portfolio Contact: {form.subject.data or '(no subject)'}"
            body = (
                f"Name: {form.name.data}\n"
                f"Email: {form.email.data}\n"
                f"Subject: {form.subject.data}\n\n"
                f"Message:\n{form.message.data}"
            )
            app = current_app._get_current_object()
            def send_async(app, api_key, recipient, email_subject, body, reply_to):
                with app.app_context():
                    try:
                        resend.api_key = api_key
                        resend.Emails.send({
                            "from": "Portfolio Contact <onboarding@resend.dev>",
                            "to": [recipient],
                            "subject": email_subject,
                            "text": body,
                            "reply_to": reply_to,
                        })
                    except Exception as e:
                        print(f"Mail error: {e}")
            threading.Thread(
                target=send_async,
                args=(app, api_key, recipient, email_subject, body, form.email.data),
                daemon=True
            ).start()

        flash('Your message has been sent! I will get back to you soon.', 'success')
        return redirect(url_for('contact.contact'))
    return render_template('contact.html', form=form)
