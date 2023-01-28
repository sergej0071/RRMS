import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { BehaviorSubject, Subscription } from 'rxjs';
import { MAX_VALUE, MIN_VALUE } from 'src/app/shared/setup-charts';

@Component({
  selector: 'app-statistic-page',
  templateUrl: './statistic-page.component.html',
  styleUrls: ['./statistic-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatisticPageComponent implements OnInit {

  public minValue: number = MIN_VALUE;
  public maxValue: number = MAX_VALUE;

  public valueControl: FormControl<number | null> = new FormControl<number>(MIN_VALUE);
  public value$: BehaviorSubject<number> = new BehaviorSubject<number>(MIN_VALUE);

  public subToValue!: Subscription;
  
  constructor() { }

  ngOnInit(): void {
    this.subToValue = this.valueControl.valueChanges.subscribe(
      (newValue: number | null) => {
        if (!(newValue && +newValue && newValue >= MIN_VALUE)) this.valueControl.setValue(MIN_VALUE);
        else if (newValue > MAX_VALUE) this.valueControl.setValue(MAX_VALUE);
        else this.value$.next(newValue)
      }
    );
  }

  ngOnDestroy() {
    this.subToValue.unsubscribe();
  }
}
