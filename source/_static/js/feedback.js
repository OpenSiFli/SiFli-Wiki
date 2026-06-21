document.addEventListener('DOMContentLoaded', function () {
    const feedbackBtn = document.getElementById('feedback-btn-link');
    if (!feedbackBtn) {
      return;
    }

    const isEnglish = (document.documentElement.getAttribute('lang') || '').toLowerCase().startsWith('en') ||
      window.location.pathname.startsWith('/en/');
    const copy = isEnglish ? {
      page: 'Page:',
      placeholder: 'Enter your feedback...',
      contactHint: 'If you would like us to contact you, please provide the following information:',
      name: 'Name',
      namePlaceholder: 'Your name',
      email: 'Email',
      emailPlaceholder: 'Your email',
      cancel: 'Cancel',
      submit: 'Submit',
      submitting: 'Submitting...',
      missingFeedback: 'Please enter your feedback.',
      incompleteContact: 'Please provide both your name and email, or leave both fields empty.',
      invalidEmail: 'Please enter a valid email address.',
      success: 'Thank you for your feedback. We will review it as soon as possible.',
      submitFailed: 'Submission failed. Please try again later.',
      networkFailed: 'Network error. Submission failed. Please try again later.'
    } : {
      page: '页面：',
      placeholder: '请输入您的反馈...',
      contactHint: '如果您希望我们与您取得联系，请提供以下信息：',
      name: '姓名',
      namePlaceholder: '您的姓名',
      email: '邮箱',
      emailPlaceholder: '您的邮箱',
      cancel: '取消',
      submit: '提交',
      submitting: '提交中...',
      missingFeedback: '请填写反馈内容',
      incompleteContact: '请同时填写您的姓名和邮箱，或者两者都留空',
      invalidEmail: '请输入有效的邮箱地址',
      success: '感谢您的反馈！我们会尽快处理。',
      submitFailed: '提交失败，请稍后重试。',
      networkFailed: '网络异常，提交失败，请稍后再试。'
    };
  
    const popup = document.createElement('div');
    popup.id = 'feedback-popup';

    // 当前页面标题
    const pageTitle = document.title;
  
    popup.innerHTML = `
      <div style="margin-bottom: 10px; font-size: 14px; color: #555;">
        ${copy.page}<strong>${pageTitle}</strong>
      </div>
      <textarea id="feedback-text" placeholder="${copy.placeholder}" rows="6"></textarea>
      <div style="margin-top: 20px; font-size: 13px; color: #333;">
        ${copy.contactHint}
      </div>
      <div class="flex-row" style="display: flex; gap: 20px; align-items: flex-start; margin-top: 8px;">
        <div style="display: flex; flex-direction: column; flex: 1; max-width: 200px;">
          <label for="feedback-name" style="margin-bottom: 4px;">${copy.name}</label>
          <input type="text" id="feedback-name" placeholder="${copy.namePlaceholder}" style="padding: 6px;" />
        </div>
        <div style="display: flex; flex-direction: column; flex: 1; max-width: 200px;">
          <label for="feedback-email" style="margin-bottom: 4px;">${copy.email}</label>
          <input type="email" id="feedback-email" placeholder="${copy.emailPlaceholder}" style="padding: 6px;" />
        </div>
      </div>
      <div class="feedback-actions">
        <button id="feedback-cancel">${copy.cancel}</button>
        <button id="feedback-submit">${copy.submit}</button>
      </div>
    `;

    document.body.appendChild(popup);
  
    feedbackBtn.onclick = (e) => {
      e.preventDefault();
      popup.style.display = 'block';
    };
  
    document.getElementById('feedback-cancel').onclick = () => popup.style.display = 'none';
    
    document.getElementById('feedback-submit').onclick = async () => {
      const submitBtn = document.getElementById('feedback-submit');
      submitBtn.disabled = true; // 禁用提交按钮
      submitBtn.textContent = copy.submitting; // 可选：显示提交中

      const name = document.getElementById('feedback-name').value.trim();
      const email = document.getElementById('feedback-email').value.trim();
      const text = document.getElementById('feedback-text').value.trim();
      if (!text) {
        alert(copy.missingFeedback);
        submitBtn.disabled = false;
        submitBtn.textContent = copy.submit;        
        return;
      }
  
      // 如果填写了姓名或邮箱，则必须同时填写且邮箱格式正确
      if ((name && !email) || (!name && email)) {
          alert(copy.incompleteContact);
          submitBtn.disabled = false;
          submitBtn.textContent = copy.submit;          
          return;
      }

      if (email) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(email)) {
              alert(copy.invalidEmail);
              submitBtn.disabled = false;
              submitBtn.textContent = copy.submit;              
              return;
          }
      }

      // 获取页面标题
      const pageTitle = document.title;
      const pageURL = window.location.href;

      // 组装请求数据
      const payload = {
          pageTitle,
          pageURL,
          feedback: text,
          name,
          email,
      };

      try {
        const response = await fetch('https://feedback.sifli.com/send_feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok && result.success) {
            alert(copy.success);
            // 清空输入框并关闭弹窗
            document.getElementById('feedback-text').value = '';
            document.getElementById('feedback-name').value = '';
            document.getElementById('feedback-email').value = '';
            popup.style.display = 'none';
        } else {
            alert(result.message || copy.submitFailed);
        }
      } catch (error) {
          alert(copy.networkFailed);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = copy.submit;
      }
    };
  });
  
