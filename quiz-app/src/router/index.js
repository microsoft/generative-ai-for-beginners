import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home.vue';
import Quiz from '@/components/Quiz.vue';
import NotFound from '@/views/NotFound.vue';
Vue.use(Router);

const router = new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/',
			name: 'home',
			component: Home,
		},
		{
			path: '/quiz/:id',
			name: 'Quiz',
			component: Quiz,
		},
		{
			path: '/:pathMatch(.*)*',
			name: 'NotFound',
			component: NotFound,
			meta: { title: 'Not Found' },
		},
	],
});

router.beforeEach((to, from, next) => {
	next();
});
export default router;
