from selenium.webdriver.common.by import By


class GlobalElements():
    class common():
        error_dialog = (By.CLASS_NAME, "dialog-error")
        success_dialog = (By.CLASS_NAME, "dialog-success")
        waring_dialog = (By.CLASS_NAME, "dialog-warning")

    class login():
        username_loc = (By.NAME, "username")
        password_loc = (By.CSS_SELECTOR, "input[type='password']")
        login_loc = (By.CLASS_NAME, "login-btn")
        login_loc_oem = (By.ID, "submit")
        check_login_loc = (By.CLASS_NAME, "error-tip")
        elements = [username_loc, password_loc, login_loc, check_login_loc]
        log_menu = (By.CSS_SELECTOR, "[name='log']")

    class mainpage():
        service_overview_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='服务概况']")
        store_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='云存储']")
        setting_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='设置']")
        service_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='服务管理']")
        client_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='应用管理']")
        devgrp_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='存储池管理']")
        block_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='块设备管理']")
        file_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='文件管理']")
        perm_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='权限管理']")
        quota_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='配额管理']")
        nas_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='NAS组管理']")
        senior_manager_menu = (By.CSS_SELECTOR, "div.menu-content[data-title='高级管理']")
        log_menu = (By.CSS_SELECTOR, "[name='log']")

    class devgrp():
        check_default = (By.CSS_SELECTOR, "td.has-split[title='default']")
        create_devgrp_loc = (By.NAME, "create-group")
        input_devgrp_name_loc = (
            By.CSS_SELECTOR, ".mb-body >form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        # input_devgrp_name_loc = (By.NAME,"name")
        input_devgrp_name_confirm = (By.CLASS_NAME, "custom-button")
        bind_dev = (By.NAME, "bind-device")
        add_dev_bynode = (By.NAME, "byNode")
        add_dev_byid = (By.NAME, "byId")
        limit_switch = (By.CLASS_NAME, "loong-switch-open")
        error_dialog = (By.CLASS_NAME, "dialog-error")
        success_dialog = (By.CLASS_NAME, "dialog-success")
        waring_dialog = (By.CLASS_NAME, "dialog-warning")
        add_dev_input_ip = (By.CLASS_NAME, "loong-search-input")
        add_dev_select_ip = (By.CSS_SELECTOR, "li.option:first-child")
        dev_list_add_submit = (By.CLASS_NAME, "custom-button")
        check_bynode_devlist = (By.CSS_SELECTOR, "td[title^='/dev']")
        bynode_devlist_firstdev = (By.CSS_SELECTOR, "td[style='padding-left: 10px;']")
        # 按照firstdev 获取同级哥哥节点 来拿到 DevID
        get_bynode_devlist_firstdevID = (By.XPATH, "//td[starts-with(@title,'/dev')]/preceding-sibling::td[1]")

    class setting():
        base_setting_menu = (By.XPATH, "//div[@id='settingLeft']/div[1]")  # 基础
        store_setting_menu = (By.XPATH, "//div[@id='settingLeft']/div[2]")  # store
        cloud_setting_menu = (By.XPATH, "//div[@id='settingLeft']/div[3]")  # cloud
        cltport_setting_menu = (By.XPATH, "//div[contains(text(),'客户端端口设置')]")
        cltport_num = (By.NAME, "port")
        cltport_save_btn = (By.NAME, "set-port")

        layout_setting_menu = (By.XPATH, "//div[contains(text(),'文件分布')]")
        getalarm_setting_menu = (By.XPATH, "//div[contains(text(),'告警订阅')]")
        netcardwarn_setting_menu = (By.XPATH, "//div[contains(text(),'网卡报警管理')]")
        license_setting_menu = (By.XPATH, "//div[contains(text(),'授权管理')]")
        # 基础设置
        user_info_setting_menu = (By.XPATH, "//div[contains(text(),'用户信息')]")
        email_setting_menu = (By.XPATH, "//div[contains(text(),'邮件服务器设置')]")
