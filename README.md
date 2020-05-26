# Recollect
Recollect is a tool for storing and searching for documents. Additionlly, it has Anki-like functonality for creating flash cards that you can review periodically.

When adding a document, Recollect makes suggestion on tags to add.

# Documents
A recollect document can have the following fields:

* title (text)
* tags (text)
* body (text)
* any number of associated URLs (which can be used to point to remote files)
* the date it was added to recollect
* any number of Anki-like question-answer pairs

# The Search Engine
The search engine is based on a Bag Of Words model using TFIDF features.