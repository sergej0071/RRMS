import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ParseApiService } from 'src/app/shared/services/parse-api.service';
import { MAX_VALUE, MIN_VALUE } from 'src/app/shared/setup-charts';

@Component({
  selector: 'app-analysis-page',
  templateUrl: './analysis-page.component.html',
  styleUrls: ['./analysis-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AnalysisPageComponent implements OnInit {

  public valueControl: FormControl<number | null> = new FormControl<number>(MIN_VALUE);

  public minValue: number = MIN_VALUE;
  public maxValue: number = MAX_VALUE;

  constructor(
    public parseApiService: ParseApiService
  ) { }

  public ngOnInit(): void {
  }

}
