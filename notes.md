**Notes:**

2019-03-25...? (forgot which day this was... w/e - git knows.)
- Seems like the place to look when fixing the problem is in the DisambiguationError
  `raise DisambiguationError(getattr(self, 'title', page['title']), may_refer_to)`
  - Maybe if I can send something else in its place, the add-on won't crash

2019-03-30
- Record some data that doesn't break the add-on
  - Use that data, and send it instead of breaking the add-on?
  - ... But how do I record that data, though?

- I could also just try to change the format of DisambiguationError()
  - Not really sure how to reformat it, though... Can't just change the return statement to a string, after all.

