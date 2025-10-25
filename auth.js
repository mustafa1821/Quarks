// Authentication JavaScript for Stock Volume Data Tracker

class AuthManager {
    constructor() {
        this.currentUser = null;
        this.initializeAuth();
    }

    initializeAuth() {
        // Check if user is already logged in
        this.checkAuthStatus();
        
        // Initialize form handlers
        this.initializeFormHandlers();
    }

    checkAuthStatus() {
        const userData = localStorage.getItem('stockTrackerUser');
        if (userData) {
            this.currentUser = JSON.parse(userData);
            this.updateUIForLoggedInUser();
        }
    }

    initializeFormHandlers() {
        // Login form
        const loginForm = document.getElementById('loginForm');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => this.handleLogin(e));
        }

        // Signup form
        const signupForm = document.getElementById('signupForm');
        if (signupForm) {
            signupForm.addEventListener('submit', (e) => this.handleSignup(e));
        }

        // Logout functionality
        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => this.logout());
        }
    }

    async handleLogin(e) {
        e.preventDefault();
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const rememberMe = document.getElementById('rememberMe')?.checked || false;

        // Show loading state
        this.showLoading(true);

        try {
            // Simulate API call
            await this.simulateAPICall();
            
            // For demo purposes, accept any email/password combination
            if (email && password) {
                const user = {
                    id: Date.now(),
                    email: email,
                    name: email.split('@')[0],
                    loginTime: new Date().toISOString()
                };

                this.currentUser = user;
                localStorage.setItem('stockTrackerUser', JSON.stringify(user));
                
                this.showSuccess('Login successful! Redirecting...');
                
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 1500);
            } else {
                this.showError('Please fill in all fields');
            }
        } catch (error) {
            this.showError('Login failed. Please try again.');
        } finally {
            this.showLoading(false);
        }
    }

    async handleSignup(e) {
        e.preventDefault();
        
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const agreeTerms = document.getElementById('agreeTerms').checked;

        // Validation
        if (!fullName || !email || !password || !confirmPassword) {
            this.showError('Please fill in all fields');
            return;
        }

        if (password !== confirmPassword) {
            this.showError('Passwords do not match');
            return;
        }

        if (password.length < 6) {
            this.showError('Password must be at least 6 characters long');
            return;
        }

        if (!agreeTerms) {
            this.showError('Please agree to the Terms of Service and Privacy Policy');
            return;
        }

        // Show loading state
        this.showLoading(true);

        try {
            // Simulate API call
            await this.simulateAPICall();
            
            const user = {
                id: Date.now(),
                email: email,
                name: fullName,
                signupTime: new Date().toISOString()
            };

            this.currentUser = user;
            localStorage.setItem('stockTrackerUser', JSON.stringify(user));
            
            this.showSuccess('Account created successfully! Redirecting...');
            
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 1500);
        } catch (error) {
            this.showError('Signup failed. Please try again.');
        } finally {
            this.showLoading(false);
        }
    }

    logout() {
        this.currentUser = null;
        localStorage.removeItem('stockTrackerUser');
        this.updateUIForLoggedOutUser();
        this.showSuccess('Logged out successfully');
        
        // Redirect to login page if on main page
        if (window.location.pathname.includes('index.html')) {
            setTimeout(() => {
                window.location.href = 'login.html';
            }, 1000);
        }
    }

    updateUIForLoggedInUser() {
        // Update navigation if on main page
        const navLinks = document.querySelector('.nav-links');
        const authButtons = document.querySelector('.auth-buttons');
        
        if (navLinks && authButtons) {
            authButtons.innerHTML = `
                <div class="user-info">
                    <div class="user-avatar">
                        ${this.currentUser.name.charAt(0).toUpperCase()}
                    </div>
                    <span>${this.currentUser.name}</span>
                </div>
                <button id="logoutBtn" class="auth-btn auth-btn-secondary">
                    <i class="fas fa-sign-out-alt"></i> Logout
                </button>
            `;
            
            // Re-attach logout event listener
            const logoutBtn = document.getElementById('logoutBtn');
            if (logoutBtn) {
                logoutBtn.addEventListener('click', () => this.logout());
            }
        }
    }

    updateUIForLoggedOutUser() {
        const authButtons = document.querySelector('.auth-buttons');
        if (authButtons) {
            authButtons.innerHTML = `
                <a href="login.html" class="auth-btn auth-btn-secondary">
                    <i class="fas fa-sign-in-alt"></i> Login
                </a>
                <a href="signup.html" class="auth-btn auth-btn-primary">
                    <i class="fas fa-user-plus"></i> Sign Up
                </a>
            `;
        }
    }

    async simulateAPICall() {
        // Simulate network delay
        return new Promise(resolve => setTimeout(resolve, 1000));
    }

    showLoading(show) {
        const submitBtn = document.querySelector('.auth-submit');
        if (submitBtn) {
            if (show) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                submitBtn.disabled = true;
            } else {
                const isLogin = window.location.pathname.includes('login');
                submitBtn.innerHTML = isLogin 
                    ? '<i class="fas fa-sign-in-alt"></i> Sign In'
                    : '<i class="fas fa-user-plus"></i> Create Account';
                submitBtn.disabled = false;
            }
        }
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showNotification(message, type) {
        // Remove existing notifications
        const existing = document.querySelector('.auth-notification');
        if (existing) {
            existing.remove();
        }

        const notification = document.createElement('div');
        notification.className = `auth-notification ${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'}"></i>
            ${message}
        `;

        // Add notification styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'error' ? 'rgba(220, 53, 69, 0.9)' : 'rgba(40, 167, 69, 0.9)'};
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 600;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        `;

        document.body.appendChild(notification);

        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // Public method to check if user is logged in
    isLoggedIn() {
        return this.currentUser !== null;
    }

    // Public method to get current user
    getCurrentUser() {
        return this.currentUser;
    }
}

// Initialize authentication when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.authManager = new AuthManager();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AuthManager;
}
