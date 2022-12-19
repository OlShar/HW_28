from selenium.webdriver.common.by import By


class AuthLocators:
    # Локатор правого, левого блока формы "Авторизация".
    page_right = (By.ID, 'page-right')
    page_left = (By.ID, 'page-left')

    # Заголовок "Авторизация".
    authorization = (By.XPATH, '//section[@id="page-right"]/div/div/h1')

    # Блок авторизации формы «Авторизация».
    card_of_auth = (By.CLASS_NAME, 'card-container__wrapper')

    # Локатор меню выбора типа аутентификации.
    menu_tub = (By.XPATH, "//div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']")
    tub_phone = (By.ID, 't-btn-tab-phone')
    tub_email = (By.ID, 't-btn-tab-mail')
    tub_login = (By.ID, 't-btn-tab-login')
    tub_ls = (By.ID, 't-btn-tab-ls')
    # Локатор активного, по умолчанию, таба выбора типа аутентификации.
    active_tub_phone = (By.XPATH, '//div[@id="t-btn-tab-phone" and @class="rt-tab rt-tab--small rt-tab--active"]')

    auth_email = (By.ID, "username")
    auth_pass_eml = (By.ID, "password")

    auth_login = (By.ID, 'username')
    auth_pass_log = (By.ID, "password")

    # Кнопка "Войти"
    auth_btn_enter = (By.ID, "kc-login")

    # Ссылка "Забыл пороль"
    forgot_password_link = (By.ID, "forgot_password")
    # Ссылка "Зарегистрироваться"
    register_link = (By.ID, 'kc-register')

    # Локатор надписи формы ввода.
    placeholder_name_of_user = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    # Поля email и пароль с заполненными данными.
    placeholder_email_passw = (By.XPATH, '//span[@class="rt-input__mask-start"]')

    # Сообщение об ошибке при аутентификации.
    error_message = (By.XPATH, '//span[@id="form-error-message"]')

    # Заголовок "Восстановление пароля".
    password_recovery = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")

    # Заголовок "Регистрация".
    registration = (By.XPATH, "//h1[contains(text(),'Регистрация')]")

    # Заголовок "Личные кабинеты".
    personal_accounts = (By.XPATH, "//*[contains(text(),'Личные кабинеты')]")

    # Поля формы "Регистрация"
    first_name = (By.NAME, 'firstName')
    last_name = (By.NAME, 'lastName')
    email_registration = (By.ID, 'address')
    address_registration = (By.XPATH, "//*[contains(text(),'Регион')]")
    passw_registration = (By.ID, 'password')
    passw_registration_confirm = (By.ID, 'password-confirm')
    registration_btn = (By.NAME, 'register')
    # Редирект на форму "Авторизация".
    redirect_auth = (By.XPATH, '//button[text()="Войти"]')

    # Локатор левого блока формы "Регистрация".
    page_left_registration = (By.ID, 'page-left')
    # Блок авторизации формы «Регистрация».
    card_of_registration = (By.CLASS_NAME, 'card-container__wrapper')
    # Блок "Имя".
    container_f_name = (By.XPATH, '//div[1][@class="rt-input-container"]')
    # Блок "Фамилия".
    container_l_name = (By.XPATH, '//div[2][@class="rt-input-container"]')
    # Блок "Подтверждение пароля".
    container_passw_confirm = (By.XPATH, '//div[@class="new-password-container"]')

    # Сообщение об ошибке заполнения поля "Имя".
    error_first_name = (By.XPATH, "//form/div[1]/div[1]/span")
    # Сообщение об ошибке заполнения поля "Фамилия".
    error_last_name = (By.XPATH, '//form/div[1]/div[2]/span')
    # Сообщение об ошибке заполнения поля "email".
    error_email = (By.XPATH, "//form/div[3]/span")
    # Сообщение об ошибке заполнения поля "Пароль".
    error_passw = (By.XPATH, '//form/div[4]/div[1]/span')
    # Сообщение об ошибке заполнения поля "Подтверждение пароля".
    error_passw_confirm = (By.XPATH, '//form/div[4]/div[2]/span')
    # Сообщение "Учётная запись уже существует"
    error_account_exists = (By.XPATH, '//h2[text()="Учётная запись уже существует"]')

    # Заголовок "Подтверждение email".
    email_confirm = (By.XPATH, "//section/div/div/h1")
