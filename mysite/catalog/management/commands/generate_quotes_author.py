from django.core.management.base import BaseCommand, CommandError

from faker import Faker

from polls.models import Quot, QuoteAuthor


class Command(BaseCommand):
    help = 'generate quotes and authors'   # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('param', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        param = options['param']

        if 10 >= param >= 1000:
            raise CommandError('Value must be greater than 10 and less then 1000')
        for _ in range(param):
            author = fake.name()
            if QuoteAuthor.objects.filter(author=author):
                author_record = QuoteAuthor.objects.get(author=author)
            else:
                born_in = fake.address()
                date_of_birth = fake.date()
                description = fake.text()
                author_record = QuoteAuthor.objects.create(
                    author=author,
                    born_in=born_in,
                    date_of_birth=date_of_birth,
                    description=description
                )
            quote = fake.text()
            Quot.objects.create(title=quote, author=author_record)
            self.stdout.write(f'Quotes for {author} success added!')
        self.stdout.write(self.style.SUCCESS('Quotes and Author success generate!'))
