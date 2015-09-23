
import pytest
from spyc.scheduler import Scheduler
from spyc.testing import SetElement, Fail, Failure


@pytest.fixture()
def the_set():
    return set()


@pytest.fixture()
def sched():
    return Scheduler()


def test_all_succeed(the_set, sched):
    sched.ensure(SetElement(1, the_set))
    sched.ensure(SetElement(2, the_set))
    sched.ensure(SetElement(3, the_set))
    sched.apply()
    assert the_set == set([1, 2, 3])


def test_failure(the_set, sched):
    sched.ensure(SetElement(1, the_set))
    sched.ensure(SetElement(2, the_set))

    sched.depend(SetElement(2, the_set), Fail(1))
    sched.depend(Fail(1), SetElement(1, the_set))

    with pytest.raises(Failure):
        sched.apply()

    assert the_set == set([1])
