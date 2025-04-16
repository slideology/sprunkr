from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, session, g
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import json
import logging

# 导入工具函数
from utils.faq_utils import get_faqs_for_page
from utils.translation_utils import get_translations

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'sprunkr-secret-key-2023')

# 导入日志配置
from config.logging_config import setup_logging

# 设置日志系统
setup_logging(app)

@app.route('/')
def home():
    translations_data = get_translations()
    faq_data = get_faqs_for_page('index')  # 使用sprunkr的FAQ数据作为主页FAQ
    return render_template('index.html',
                         page_title='Sprunki Sprunkr',
                         title='Sprunkr - Interactive Music Experience',
                         description='Create amazing music with Sprunkr! Mix beats, compose tunes, and share your musical creations.',
                         translations=translations_data,
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'])

@app.route('/about')
def about():
    try:
        trans = get_translations()
        return render_template('about.html', 
                         title='About Sprunkr',
                         translations=trans)
    except Exception as e:
        app.logger.error(f"Error in about route: {e}")
        return render_template('about.html',
                         title='About Sprunkr',
                         translations={
                             "nav": {"home": "Home", "faq": "FAQ"},
                             "hero": {
                                 "title_highlight": "Create Music",
                                 "title_regular": "Like Never Before",
                                 "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
                             }
                         })

@app.route('/game')
def game():
    try:
        trans = get_translations()
        return render_template('game.html',
                         title='Play Sprunkr',
                         translations=trans)
    except Exception as e:
        app.logger.error(f"Error in game route: {e}")
        return render_template('game.html',
                         title='Play Sprunkr',
                         translations={
                             "nav": {"home": "Home", "faq": "FAQ"},
                             "hero": {
                                 "title_highlight": "Create Music",
                                 "title_regular": "Like Never Before",
                                 "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
                             }
                         })

@app.route('/introduction')
def introduction():
    try:
        trans = get_translations()
        return render_template('introduction.html',
                         title='Game Guide - Sprunkr',
                         translations=trans)
    except Exception as e:
        app.logger.error(f"Error in introduction route: {e}")
        return render_template('introduction.html',
                         title='Game Guide - Sprunkr',
                         translations={
                             "nav": {"home": "Home", "faq": "FAQ"},
                             "hero": {
                                 "title_highlight": "Create Music",
                                 "title_regular": "Like Never Before",
                                 "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
                             }
                         })

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    try:
        trans = get_translations()
        if request.method == 'POST':
            return send_message()
        return render_template('contact.html',
                         title='Contact Sprunkr',
                         translations=trans)
    except Exception as e:
        app.logger.error(f"Error in contact route: {e}")
        return render_template('contact.html',
                         title='Contact Sprunkr',
                         translations={
                             "nav": {"home": "Home", "faq": "FAQ"},
                             "hero": {
                                 "title_highlight": "Create Music",
                                 "title_regular": "Like Never Before",
                                 "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
                             }
                         })

@app.route('/faq')
def faq():
    try:
        trans = get_translations()
        return render_template('faq.html',
                         title='FAQ - Sprunkr',
                         translations=trans)
    except Exception as e:
        app.logger.error(f"Error in faq route: {e}")
        return render_template('faq.html',
                         title='FAQ - Sprunkr',
                         translations={
                             "nav": {"home": "Home", "faq": "FAQ"},
                             "hero": {
                                 "title_highlight": "Create Music",
                                 "title_regular": "Like Never Before",
                                 "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
                             }
                         })

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('static', 'ads.txt')

@app.route('/sprunki-lily')
def sprunki_lily():
    faq_data = get_faqs_for_page('sprunki-lily')
    return render_template('sprunki-lily.html',
                         page_title='Sprunki Lily',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-1996')
def sprunki_1996():
    """Sprunki 1996游戏页面路由"""
    faq_data = get_faqs_for_page('sprunki-1996')
    return render_template('sprunki-1996.html',
                          page_title='Sprunki 1996',
                          dynamic_faqs=faq_data['faqs'],
                          conclusion=faq_data['conclusion'],
                          translations=get_translations())

@app.route('/sprunki-shatter')
def sprunki_shatter():
    faq_data = get_faqs_for_page('sprunki-shatter')
    return render_template('sprunki-shatter.html',
                         page_title='Sprunki Shatter',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())                         

@app.route('/sprunki-fiddlebops')
def sprunki_fiddlebops():
    faq_data = get_faqs_for_page('sprunki-fiddlebops')
    return render_template('sprunki-fiddlebops.html',
                         page_title='Sprunki Fiddlebops',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/incredibox-rainbow-animal')
def incredibox_rainbow_animal():
    faq_data = get_faqs_for_page('incredibox-rainbow-animal')
    return render_template('incredibox-rainbow-animal.html',
                         page_title='Incredibox Rainbow Animal',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/incredibox-irrelevant-reunion')
def incredibox_irrelevant_reunion():
    faq_data = get_faqs_for_page('incredibox-irrelevant-reunion')
    return render_template('incredibox-irrelevant-reunion.html',
                         page_title='Incredibox Irrelevant Reunion',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-misfismix')
def sprunki_misfismix():
    faq_data = get_faqs_for_page('sprunki-misfismix')
    return render_template('sprunki-misfismix.html',
                         page_title='Sprunki Misfismix',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunka')
def sprunka():
    faq_data = get_faqs_for_page('sprunka')
    return render_template('sprunka.html',
                         page_title='Sprunka',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-6-definitive-all-alive')
def sprunki_phase_6_definitive_all_alive():
    faq_data = get_faqs_for_page('sprunki-phase-6-definitive-all-alive')
    return render_template('sprunki-phase-6-definitive-all-alive.html',
                         page_title='Sprunki Phase 6 Definitive All Alive',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-6-definitive-remaster')
def sprunki_phase_6_definitive_remaster():
    faq_data = get_faqs_for_page('sprunki-phase-6-definitive-remaster')
    return render_template('sprunki-phase-6-definitive-remaster.html',
                         page_title='Sprunki Phase 6 Definitive Remaster',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-6-definitive')
def sprunki_phase_6_definitive():
    faq_data = get_faqs_for_page('sprunki-phase-6-definitive')
    return render_template('sprunki-phase-6-definitive.html',
                         page_title='Sprunki Phase 6 Definitive',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-sploinkers')
def sprunki_sploinkers():
    faq_data = get_faqs_for_page('sprunki-sploinkers')
    return render_template('sprunki-sploinkers.html',
                         page_title='Sprunki Sploinkers',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-pyramixed-regretful')
def sprunki_pyramixed_regretful():
    faq_data = get_faqs_for_page('sprunki-pyramixed-regretful')
    return render_template('sprunki-pyramixed-regretful.html',
                         page_title='Sprunki Pyramixed Regretful',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-megalovania')
def sprunki_megalovania():
    faq_data = get_faqs_for_page('sprunki-megalovania')
    return render_template('sprunki-megalovania.html',
                         page_title='Sprunki Megalovania',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-sprunkr')
def sprunki_sprunkr():
    faq_data = get_faqs_for_page('sprunki-sprunkr')
    return render_template('sprunki-sprunkr.html',
                         page_title='Sprunkr',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-brud-edition-finale')
def sprunki_brud_edition_finale():
    faq_data = get_faqs_for_page('sprunki-brud-edition-finale')
    return render_template('sprunki-brud-edition-finale.html',
                         page_title='Sprunki Brud Edition Finale',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-spruted')
def sprunki_spruted():
    faq_data = get_faqs_for_page('sprunki-spruted')
    return render_template('sprunki-spruted.html',
                         page_title='Sprunki Spruted',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-spfundi')
def sprunki_spfundi():
    faq_data = get_faqs_for_page('sprunki-spfundi')
    return render_template('sprunki-spfundi.html',
                         page_title='Sprunki Spfundi',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-angry')
def sprunki_angry():
    faq_data = get_faqs_for_page('sprunki-angry')
    return render_template('sprunki-angry.html',
                         page_title='Sprunki Angry',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-777-3-7')
def sprunki_phase_777_3_7():
    faq_data = get_faqs_for_page('sprunki-phase-777-3-7')
    return render_template('sprunki-phase-777-3-7.html',
                         page_title='Sprunki Phase 777 3.7',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunklings')
def sprunklings():
    faq_data = get_faqs_for_page('sprunki-sprunklings')
    return render_template('sprunklings.html',
                         page_title='Sprunklings',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-swap-retextured')
def sprunki_swap_retextured():
    faq_data = get_faqs_for_page('sprunki-swap-retextured')
    return render_template('sprunki-swap-retextured.html',
                         page_title='Sprunki Swap Retextured',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-upin-ipin')
def sprunki_upin_ipin():
    faq_data = get_faqs_for_page('sprunki-upin-ipin')
    return render_template('sprunki-upin-ipin.html',
                         page_title='Sprunki Upin Ipin',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-ultimate-deluxe')
def sprunki_ultimate_deluxe():
    faq_data = get_faqs_for_page('sprunki-ultimate-deluxe')
    return render_template('sprunki-ultimate-deluxe.html',
                         page_title='Sprunki Ultimate Deluxe',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-19-update')
def sprunki_phase_19_update():
    faq_data = get_faqs_for_page('sprunki-phase-19-update')
    return render_template('sprunki-phase-19-update.html',
                         page_title='Sprunki Phase 19 Update',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-phase-1-7')
def sprunki_phase_1_7():
    faq_data = get_faqs_for_page('sprunki-phase-1-7')
    return render_template('sprunki-phase-1-7.html',
                         page_title='Sprunki Phase 1.7',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-dx')
def sprunki_dx():
    faq_data = get_faqs_for_page('sprunki-dx')
    return render_template('sprunki-dx.html',
                         page_title='Sprunki DX',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-banana')
def sprunki_banana():
    faq_data = get_faqs_for_page('sprunki-banana')
    return render_template('sprunki-banana.html',
                         page_title='Sprunki Banana',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-garnold')
def sprunki_garnold():
    faq_data = get_faqs_for_page('sprunki-garnold')
    return render_template('sprunki-garnold.html',
                         page_title='Sprunki Garnold',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-ketchup')
def sprunki_ketchup():
    faq_data = get_faqs_for_page('sprunki-ketchup')
    return render_template('sprunki-ketchup.html',
                         page_title='Sprunki Ketchup',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-sprunksters')
def sprunki_sprunksters():
    faq_data = get_faqs_for_page('sprunki-sprunksters')
    return render_template('sprunki-sprunksters.html',
                         page_title='Sprunki Sprunksters',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-agents')
def sprunki_agents():
    faq_data = get_faqs_for_page('sprunki-agents')
    return render_template('sprunki-agents.html',
                         page_title='Sprunki Agents',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-banana-porridge')
def sprunki_banana_porridge():
    faq_data = get_faqs_for_page('sprunki-banana-porridge')
    return render_template('sprunki-banana-porridge.html',
                         page_title='Sprunki Banana Porridge',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-retake-but-human')
def sprunki_retake_but_human():
    faq_data = get_faqs_for_page('sprunki-retake-but-human')
    return render_template('sprunki-retake-but-human.html',
                         page_title='Sprunki Retake But Human',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-retake-new-human')
def sprunki_retake_new_human():
    faq_data = get_faqs_for_page('sprunki-retake-new-human')
    return render_template('sprunki-retake-new-human.html',
                         page_title='Sprunki Retake New Human',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())
@app.route('/sprunki-grown-up')
def sprunki_grown_up():
    faq_data = get_faqs_for_page('sprunki-grown-up')
    return render_template('sprunki-grown-up.html',
                         page_title='Sprunki Grown Up',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-parodybox')
def sprunki_parodybox():
    faq_data = get_faqs_for_page('sprunki-parodybox')
    return render_template('sprunki-parodybox.html',
                         page_title='Sprunki ParodyBox',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/sprunki-pyramixed')
def sprunki_pyramixed():
    faq_data = get_faqs_for_page('sprunki-pyramixed')
    return render_template('sprunki-pyramixed.html',
                         page_title='Sprunki PyraMixed',
                         dynamic_faqs=faq_data['faqs'],
                         conclusion=faq_data['conclusion'],
                         translations=get_translations())

@app.route('/privacy-policy')
def privacy_policy():
    try:
        translations_data = get_translations()
        return render_template('privacy-policy.html', translations=translations_data)
    except Exception as e:
        app.logger.error(f"Error in privacy policy route: {e}")
        return render_template('error.html', error="An error occurred loading the privacy policy page.")

@app.route('/terms-of-service')
def terms_of_service():
    try:
        translations_data = get_translations()
        return render_template('terms-of-service.html', translations=translations_data)
    except Exception as e:
        app.logger.error(f"Error in terms of service route: {e}")
        return render_template('error.html', error="An error occurred loading the terms of service page.")

def send_message():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not all([name, email, subject, message]):
            flash('Please fill in all fields', 'error')
            return redirect(url_for('contact'))
        
        try:
            email_user = os.getenv('EMAIL_USER')
            email_password = os.getenv('EMAIL_PASSWORD')
            
            if not email_user or not email_password:
                flash('Email configuration is not set up', 'error')
                return redirect(url_for('contact'))
            
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_user  # Send to yourself
            msg['Subject'] = f"Sprunkr: {subject} - from {name}"
            
            body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
            server.quit()
            
            flash('Thank you for your message! We will get back to you soon.', 'success')
        except Exception as e:
            app.logger.error(f"Error sending message: {str(e)}")
            flash('Sorry, there was a problem sending your message. Please try again later.', 'error')
    except Exception as e:
        app.logger.error(f"Error in send_message: {e}")
        flash('Sorry, there was a problem sending your message. Please try again later.', 'error')
    
    return redirect(url_for('contact'))

# 添加全局错误处理器
@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f'Server Error: {error}')
    return render_template('error.html', 
                         error_code=500,
                         error_message="Internal Server Error",
                         translations=get_translations()), 500

@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(f'Page not found: {error}')
    return render_template('error.html', 
                         error_code=404,
                         error_message="Page Not Found",
                         translations=get_translations()), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
