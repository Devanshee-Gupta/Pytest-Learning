## Filter Tests

As your test suite grows, you may find that you want to run just a few tests on a feature and save the full suite for later. pytest provides a few ways of doing this:

1. **Name-based filtering**: You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
2. **Directory scoping**: By default, pytest will run only those tests that are in or under the current directory.
3. **Test categorization**: pytest can include or exclude tests from particular categories that you define. You can do this with the -m parameter.

Test categorization in particular is a subtly powerful tool. pytest enables you to create marks, or custom labels, for any test you like.

# Marks

pytest enables you to define categories for your tests and provides options for including or excluding categories when you run your suite. You can mark a test with any number of categories.  
Marking tests is useful for categorizing tests by subsystem or dependencies. If some of your tests require access to a database, for example, then you could create a @pytest.mark.database_access mark for them.
If you’d like to run only those tests that require database access, then you can use pytest -m database_access. To run all tests except those that require database access, you can use pytest -m "not database_access".

> You can use the --strict-markers flag to the pytest command to ensure that all marks in your tests are registered in your pytest configuration file, pytest.ini. It’ll prevent you from running your tests until you register any unknown marks.

Pytest provides a few marks out of the box:
1. **skip** - skips a test unconditionally.
2. **skipif** - skips a test if the expression passed to it evaluates to True.
3. **xfail** - indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.
4. **parametrize** - creates multiple variants of a test with different values as arguments. You’ll learn more about this mark shortly.
