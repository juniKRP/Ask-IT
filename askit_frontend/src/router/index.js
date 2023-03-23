import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import QuestionView from '@/views/QuestionView.vue'
import AskView from '@/views/AskView.vue'
import AboutView from "@/views/AboutView.vue";
import ModuleView from "@/views/ModuleView.vue";
import PrivacyView from "@/views/PrivacyView.vue";
import SearchView from "@/views/SearchView.vue";
import AdvancedSearchView from "@/views/AdvancedSearchView.vue";

const routes = [
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: '/privacy',
        name: 'privacy',
        component: PrivacyView
    },
    {
        path: '/question/:id',
        name: 'question',
        component: QuestionView,
    },
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/ask/:mod',
        name: 'ask',
        component: AskView
    },
    {
        path: '/module/:mod',
        name: 'module',
        component: ModuleView
    },
    {
        path: '/search/',
        name: 'search',
        component: SearchView
    },
    {
        path: '/advanced-search/',
        name: 'advanced-search',
        component: AdvancedSearchView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
