
**retrieve.md**
```markdown
# Retrieve Book

```python
from bookshelf.models import Book
Book.objects.get()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
