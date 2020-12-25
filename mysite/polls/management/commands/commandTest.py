from django.core.management.base import BaseCommand

from faker import Faker

from polls.models import Person

fake = Faker()


class Command(BaseCommand):
    help = 'generate random users'   # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('param', type=int)

    def handle(self, *args, **options):
        param = options.get('param')

        if 1 <= param <= 10:
            for i in range(param):
                p = Person.objects.create(username=fake.name(), email=fake.email(), password=fake.password())
                print(p)   # noqa: T001
        else:
            raise AssertionError
        self.stdout.write(self.style.SUCCESS('Successful!'))
