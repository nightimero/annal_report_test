# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
import pytest
import env
# import utils
import requests
import my_testdata
import mysql_data


@pytest.fixture()
def save_the_symptom(content):
    """
    登录并保存病症
    :return:
    """
    # 登录
    req = requests.Session()
    r = req.post(env.URL + "/user/login", headers=env.headers,
                 data=json.dumps({"mobile": env.USERNAME, "password": env.PASSWD}))
    # 保存病例
    r = req.post(env.URL + "/patientCase/savePatientCaseQA", headers=env.headers, data=json.dumps(content))
    result = json.loads(r.text)
    print json.dumps(result, encoding='UTF-8', ensure_ascii=False)
    return result


class TestLDH(object):
    # 初始化用户数据
    def setup(self):
        gender = my_testdata.all_factors_gender
        birthday = my_testdata.all_factors_birthday
        mysql_data.insert_user_data_into_mysql(env.UID, env.USERNAME, gender, birthday)
        print env.UID

    def test_all_factors(self):
        content = my_testdata.all_factors_request
        result = save_the_symptom(content)
        assert result["body"]["data"] == u'操作成功'
        assert result["code"] == 1
        assert result["message"] == u'成功'
        (disease, disease_probability) = mysql_data.get_dignose_disease(env.UID)
        print json.dumps((disease, disease_probability), encoding='UTF-8', ensure_ascii=False)
        assert disease == u'腰椎间盘突出症'
        # todo:bug概率不对。
        assert disease_probability == 0.94


if __name__ == "__main__":
    print pytest.main("-q all.py -s -v")

