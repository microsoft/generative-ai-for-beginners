import Vue from 'vue';
import App from './App.vue';
Vue.config.productionTip = false;
import router from './router';

import VueI18n from 'vue-i18n';
Vue.use(VueI18n);

const i18n = new VueI18n({
	locale: 'en',
	fallbackLocale: 'en',
});

new Vue({ i18n, router, render: (h) => h(App) }).$mount('#app');
