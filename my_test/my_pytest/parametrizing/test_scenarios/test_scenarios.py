# -*- coding:utf-8 -*-
def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append(([x[1] for x in items]))
    print "argnames is: ", argnames
    print "argvalues is: ", argvalues
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


scenario1 = ('basic', {'attribute': 'value'})
scenario2 = ('advanced', {'attribute': 'value2'})


class TestSampleWithScenarios(object):
    scenarios = [scenario1, scenario2]

    def test_demo1(self, attribute):
        # print attribute
        assert isinstance(attribute, str)

    def test_demo2(self, attribute):
        assert isinstance(attribute, str)

# $ pytest --collect-only test_scenarios.py