import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { Observable, map, timer } from 'rxjs';

@Component({
  selector: 'app-current-page',
  templateUrl: './current-page.component.html',
  styleUrls: ['./current-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CurrentPageComponent implements OnInit {

  public time$!: Observable<Date>;

  constructor() { }

  ngOnInit(): void {
    this.time$ = timer(0, 1000).pipe(
      map(() => new Date()));
  }

}
