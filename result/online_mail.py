import datetimeimport os, os.pathfrom time import sleepimport smtplibfrom email.mime.image import MIMEImagefrom email.mime.multipart import MIMEMultipartfrom email.mime.text import MIMETextfrom email.header import Headerimport imgkitimport logginglogger = logging.getLogger(__name__)def sendEmail(img):    logger.info('开始邮件发送')    sender = 'qding@qding.me'    pwd = 'abc123c'    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱    receivers = ['all@qding.me']    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)    timeresult = runTime.strftime("%Y-%m-%d %H:%M:%S")    msgRoot = MIMEMultipart('related')    msgRoot['From'] = Header("【千丁质量】", 'utf-8')    msgRoot['To'] = Header("千丁All", 'utf-8')    subject = '【千丁】各系统上线发布公告: ' + str(timeresult)    msgRoot['Subject'] = Header(subject, 'utf-8')    msgAlternative = MIMEMultipart('alternative')    msgRoot.attach(msgAlternative)    mail_msg = '''    <h2>千丁.各系统上线发布公告：    ''' + str(timeresult) + '''</h2>    <p><img src="cid:image1"></p>    '''    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))    msgImage = MIMEImage(img)    # 定义图片 ID，在 HTML 文本中引用    msgImage.add_header('Content-ID', '<image1>')    msgRoot.attach(msgImage)    logger.info('邮件发送……')    try:        smtpObj = smtplib.SMTP('smtp.exmail.qq.com')        smtpObj.login(sender, pwd)        smtpObj.sendmail(sender, receivers, msgRoot.as_string())        logger.info(str(receivers) + '邮件发送成功')    except smtplib.SMTPException:        logger.error("Error: 无法发送邮件")def htmlToImg():    # file = 'out.jpg'    # if (os.path.exists(file)):  # 检查指定文件是否存在,如果存在就删除    #     os.remove(file)    #     sleep(10)    #     logger.info('删除成功')    img = imgkit.from_url('http://sniffer.iqdnet.cn/misoa/today_online_mail/', False)    logger.info('文件获取成功')    sendEmail(img)    logger.info('图片截取成功，发送图片完成')    return '邮件发送成功'