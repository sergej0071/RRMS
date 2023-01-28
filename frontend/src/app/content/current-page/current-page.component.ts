import { Component, OnInit } from '@angular/core';
import { Observable, interval, map } from 'rxjs';

@Component({
  selector: 'app-current-page',
  templateUrl: './current-page.component.html',
  styleUrls: ['./current-page.component.scss']
})
export class CurrentPageComponent implements OnInit {

  public time$!: Observable<Date>;

  constructor() { }

  ngOnInit(): void {
    this.time$ = interval(1000).pipe(
      map(() => new Date()));
  }

}
