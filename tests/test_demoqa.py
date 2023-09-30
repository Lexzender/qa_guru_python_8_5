import os
from selene import browser, have , command



def test_Positive_Student_Registration_Form():

    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Aleksei")
    browser.element("#lastName").type("Kostromin")
    browser.element("#userEmail").type("test@mail.ru")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("8927761453")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element('option[value="4"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1994"]').click()
    browser.element(".react-datepicker__day--020").click()
    browser.element("#subjectsInput").type("Com")
    browser.all(".subjects-auto-complete__menu-list").first.click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('file/test.txt'))
    browser.element("#currentAddress").type("some text")
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.all(".css-11unzgr").element_by(have.text("Haryana")).click()
    browser.element("#city").click()
    browser.all(".css-11unzgr").element_by(have.text("Panipat")).click()
    browser.element("#submit").click()
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
        'Aleksei Kostromin',
        'test@mail.ru',
        'Male',
        '8927761453',
        '20 May,1994',
        'Computer Science',
        'Music',
        'test.txt',
        'some text',
        'Haryana Panipat'
    ))


