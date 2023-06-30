import os

from selene import browser, have, be, command
from selenium.webdriver.common.by import By
#from qa_guru_6_5.conditions import match

def test_registration_form():
    browser.open('/automation-practice-form')
    #Заполняем ФИ, email,пол,номер
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Dasha')
    browser.element('#lastName').type('Kirillova')
    browser.element('#userEmail').type('dasha@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('7999999999')
    #Заполняем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2000"]').click()
    browser.element('.react-datepicker__day--015').click()
    #Заполняем предмет, хобби
    browser.element('#subjectsInput').type('ec')
    browser.all("#subjectsWrapper div").element_by(have.exact_text("Economics")).click()
    browser.all('#hobbiesWrapper label').element_by(have.exact_text('Music')).click()
    #Загружаем изображение
    browser.element('#uploadPicture').send_keys(os.path.abspath("file/кубик-рубика.jpg"))
    #Заполняем адрес
    browser.element('#currentAddress').type('test123')
    browser.execute_script("return document.body.scrollHeight > window.innerHeight")

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').perform(command.js.click)


    #Форма с заполненными полями
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive>table>tbody>tr').should((have.size(10)))

    #Проверяем заполненость полей валидными данными
    browser.element('.modal-body').should(have.text('Dasha Kirillova'))
    browser.element('.modal-body').should(have.text('dasha@mail.ru'))
    browser.element('.modal-body').should(have.text('Female'))
    browser.element('.table-responsive tr:nth-child(4) td:nth-child(1)').should(have.exact_text('Mobile'))
    browser.element('.table-responsive tr:nth-child(4) td:nth-child(2)').should(have.exact_text('7999999999'))
    browser.element('.table-responsive tr:nth-child(5) td:nth-child(1)').should(have.exact_text('Date of Birth'))
    browser.element('.table-responsive tr:nth-child(5) td:nth-child(2)').should(have.text('15 June,2000'))
    browser.element('.table-responsive').should(have.text('Economics'))

    browser.element('.modal-body').should(have.text('Music'))

    browser.element('.modal-body').should(have.text('кубик-рубика.jpg'))
    browser.element('.modal-body').should(have.text('test123'))
    browser.element('.modal-body').should(have.text('NCR Delhi'))

    #Закрываем форму с заполненными данными
    browser.element('[id="closeLargeModal"]').click()

    #После закрытия формы проверяем что форма регистрация пуста
    browser.element('#firstName').should(be.blank)













