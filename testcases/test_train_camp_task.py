from testcases import *


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('高级群发--群聊群发')
def test_create_gaoji_group_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampGaoJiGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('高级群发--私聊群发--按条件')
def test_create_gaoji_person_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampGaoJiPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('高级群发--私聊群发--按到课')
def test_create_gaoji_person_2_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampGaoJiPersonData_2.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('智能语音--按到课')
def test_create_gaoji_person_2_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampVoiceData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('智能语音--按条件')
def test_create_gaoji_person_2_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampVoiceData_2.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('高级群发--群公告')
def test_create_gaoji_notice_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampGaoJiNoticeData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('高级群发--群聊群发--指定的群单独发送')
def test_gaoji_create_group_one_by_one_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampGaoJiGroupDataOneByOne.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('极速群发--群聊群发')
def test_create_jisu_group_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampJiSuGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('智能助理SOP')
@allure.title('极速群发--私聊群发')
def test_create_jisu_person_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.train_camp_page.navigate()
    data = TrainCampJiSuPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.train_camp_page.create_task_func(**data)
