import { Routes } from '@angular/router';
import { Home } from '@app/page/home/home';

export const routes: Routes = [
    {
        title: 'Home',
        path: '',
        component: Home,
        pathMatch: 'full',
    },
    {
        path: '**',
        redirectTo: '',
    }
];
