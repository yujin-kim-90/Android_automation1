import smtplib
from email.mime.text import MIMEText

# (*)보낼 메일의 내용과 제목
content = """
임시 내용
"""
title = '메일 제목'

msg = MIMEText(content)
msg['Subject'] = title

sender = 'aaaqwww149@gmail.com'
receiver = ['yujinkim@lottecard.co.kr']
app_password = 'qahf jhpp fqgl ugim'


# 세션 생성
with smtplib.SMTP('smtp.gmail.com', 587) as s:
    s.starttls()

# 로그인 인증과 메일 보내기
    s.login(sender, app_password)
    s.sendmail(sender, receiver, "hi")
    s.quit()

