import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ARTICLES } from 'src/app/shared/articles';
import { IArticle } from 'src/app/shared/interfaces';

@Component({
  selector: 'app-help-page',
  templateUrl: './help-page.component.html',
  styleUrls: ['./help-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HelpPageComponent {

  public atricles: IArticle[] = ARTICLES;

}
