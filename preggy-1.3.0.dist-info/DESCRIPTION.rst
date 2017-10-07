preggy is an assertion library for Python. (What were you ``expect()``ing?)


EXAMPLE
=======

    from preggy import expect

    def test_roses_are_red():
        rose = Rose()
        expect(rose.color).to_equal('red')

    def test_violets_are_not_red():
        violet = Violet()
        expect(violet.color).not_to_equal('red')


For more info:
http://heynemann.github.io/preggy



