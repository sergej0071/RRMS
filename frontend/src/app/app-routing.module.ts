import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalysisPageComponent } from './content/analysis-page/analysis-page.component';
import { CurrentPageComponent } from './content/current-page/current-page.component';
import { HelpPageComponent } from './content/help-page/help-page.component';
import { StatisticPageComponent } from './content/statistic-page/statistic-page.component';

const routes: Routes = [
  { path: '', redirectTo: '/current', pathMatch: 'full' },
  { path: 'current', component: CurrentPageComponent },
  { path: 'statistic', component: StatisticPageComponent },
  { path: 'analysis', component: AnalysisPageComponent },
  { path: 'help', component: HelpPageComponent },
  { path: '**', redirectTo: 'current' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
