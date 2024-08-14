from celery import shared_task
from .models import Application, Answer
from template.models import ApplicationQuestion

@shared_task
def process_application(application_id, answers):
    try:
        print(f"Received application_id: {application_id}")
        applyContent = Application.objects.get(id=application_id)

        print(f"Application {application_id} found.")

        for question_id, answer_text in answers.items():
            print(f"Processing question {question_id} with answer '{answer_text}'")
            question = ApplicationQuestion.objects.get(id=question_id)
            Answer.objects.create(
                application = applyContent,
                question = question,
                answer_text = answer_text,
            )

        applyContent.status = 'submitted'
        applyContent.save()

        return f"Application {application_id} processed successfully"
    except Application.DoesNotExist:
        return f"Application {application_id} does not exist"
    except ApplicationQuestion.DoesNotExist:
        return f"Question {question_id} does not exist"