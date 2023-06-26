from django.contrib.postgres.aggregates import ArrayAgg, StringAgg
from django.db.models import F, OuterRef, Prefetch, Q, Subquery, Value

from .models import (
    BooksAuthor,
    BooksBook,
    BooksBookAuthors,
    BooksBookBookshelves,
    BooksBookLanguages,
    BooksBookSubjects,
    BooksFormat,
)


def get_books(
    book_id=None, language=None, mime_type=None, topic=None, author=None, title=None
):
    books = BooksBook.objects.all()

    if book_id is not None:
        book_ids = book_id.split(",")
        books = books.filter(gutenberg_id__in=book_ids)

    if language is not None:
        languages = language.split(",")
        language_qs = BooksBookLanguages.objects.filter(
            language__code__in=languages
        ).values_list("book_id", flat=True)
        books = books.filter(pk__in=language_qs)

    if mime_type is not None:
        mime_types = mime_type.split(",")
        mime_type_qs = BooksFormat.objects.filter(mime_type__in=mime_types).values_list(
            "book_id", flat=True
        )
        books = books.filter(pk__in=mime_type_qs)

    if topic is not None:
        topics = topic.split(",")
        subject_qs = Q()
        bookshelf_qs = Q()
        for item in topics:
            subject_qs = subject_qs | Q(subject__name__icontains=item)
            bookshelf_qs = bookshelf_qs | Q(bookshelf__name__icontains=item)
        subject_qs_list = BooksBookSubjects.objects.filter(subject_qs).values_list(
            "book_id", flat=True
        )
        bookshelf_qs_list = BooksBookBookshelves.objects.filter(
            bookshelf_qs
        ).values_list("book_id", flat=True)

        books = books.filter(Q(pk__in=subject_qs_list) | Q(pk__in=bookshelf_qs_list))

    if author is not None:
        authors = author.split(",")
        author_qs = Q()
        for item in authors:
            author_qs = author_qs | Q(author__name__icontains=item)
        author_qs = BooksBookAuthors.objects.filter(author_qs).values_list(
            "book_id", flat=True
        )
        books = books.booksbookauthors_set().filter(author_qs)
        # books = books.filter(pk__in=author_qs)

    if title is not None:
        titles = title.split(",")
        title_qs = Q()
        for item in titles:
            title_qs = title_qs | Q(title__icontains=item)

        books = books.filter(title_qs)

    language_sub_qs = BooksBookLanguages.objects.filter(book_id=OuterRef("pk"))
    books = books.annotate(
        language=Subquery(language_sub_qs.values("language__code")[:1])
    )

    subjects_sub_qs = BooksBookSubjects.objects.filter(book_id=OuterRef("pk"))
    books = books.annotate(
        subjects=Subquery(
            subjects_sub_qs.values("book_id")
            .annotate(subs=ArrayAgg("subject__name"))
            .values("subs")[:1]
        )
    )

    bookshelf_sub_qs = BooksBookBookshelves.objects.filter(book_id=OuterRef("pk"))
    books = books.annotate(
        bookshelves=Subquery(
            bookshelf_sub_qs.values("book_id")
            .annotate(shelfs=ArrayAgg("bookshelf__name"))
            .values("shelfs")[:1]
        )
    )

    urls_sub_qs = BooksFormat.objects.filter(book_id=OuterRef("pk"))
    books = books.annotate(
        urls=Subquery(
            urls_sub_qs.values("book_id")
            .annotate(url=ArrayAgg("url"))
            .values("url")[:1]
        )
    )

    bookauthor_sub_qs = BooksBookAuthors.objects.filter(book_id=OuterRef("pk"))
    books = books.annotate(
        author=Subquery(bookauthor_sub_qs.values("author__name")[:1])
    )

    books = books.order_by(F("download_count").desc(nulls_last=True))
    books = books.values(
        "id",
        "title",
        "language",
        "author",
        "subjects",
        "bookshelves",
        "urls",
    )
    return books
