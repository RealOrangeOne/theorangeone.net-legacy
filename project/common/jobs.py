from mail_templated import send_mail


def send_email(job):
    template = job.workspace['template']
    context = job.workspace['context'] or {}
    to_email = job.workspace['to_email']
    from_email = job.workspace['from_email']

    if type(to_email) != list:
        to_email = [to_email]

    send_mail(template, context, from_email, to_email)
