from ._basestaff import BasicCommand


class Command(BasicCommand):

    help = "Command Line Script for Change Staff Users for is Staff"

    def handle(self, *args, **options):
        user = super().handle(*args, **options)
        user.is_staff = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Changed Staff {options['username']} User")
        )
