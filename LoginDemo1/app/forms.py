#!/usr/bin/env python
#coding:utf-8
class LoginForm(Form):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录', default = False)
    submit = SubmitField('登录')
