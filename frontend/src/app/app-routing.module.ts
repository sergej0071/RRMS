import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CurrentPageComponent } from './content/current-page/current-page.component';
import { HelpPageComponent } from './content/help-page/help-page.component';
import { StatisticPageComponent } from './content/statistic-page/statistic-page.component';

const routes: Routes = [
  { path: '', redirectTo: '/current', pathMatch: 'full' },
  { path: 'current', component: CurrentPageComponent },
  { path: 'statistic', component: StatisticPageComponent },
  { path: 'help', component: HelpPageComponent },
  { path: '**', redirectTo: 'current' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
