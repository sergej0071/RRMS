import { FormControl } from "@angular/forms";
import { BehaviorSubject, EMPTY } from "rxjs"
import { MAX_VALUE, MIN_VALUE } from "src/app/shared/setup-charts";
import { StatisticPageComponent } from "./statistic-page.component";

describe('StatisticPageComponent', () => {

  let statisticPageComponent: StatisticPageComponent;
  let valueControl: FormControl<number | null>;
  let value$: BehaviorSubject<number>;

  beforeEach(() => {
    const spy = jasmine.createSpyObj('ParseApiService', { getLastValues: EMPTY });
    statisticPageComponent = new StatisticPageComponent(spy);
    statisticPageComponent.ngOnInit();
    valueControl = statisticPageComponent.valueControl;
    value$ = statisticPageComponent.value$;
  });

  it(`should value be equal to ${MIN_VALUE}`, () => {
    expect(value$.getValue()).toBe(MIN_VALUE);
  });

  it('should value be equal to 451', () => {
    valueControl.setValue(451);
    expect(value$.getValue()).toBe(451);
  });

  it('should value be equal to 12', () => {
    valueControl.setValue(12);
    expect(value$.getValue()).toBe(12);
  });

  it('should value be equal to 25', () => {
    valueControl.setValue(25);
    expect(value$.getValue()).toBe(25);
  });

  it('should value be equal to 127', () => {
    valueControl.setValue(127);
    expect(value$.getValue()).toBe(127);
  });

  it('should value be equal to 100 random tests', () => {
    for (let i = 0; i < 100; i++) {
      const randomNum = Math.round(Math.random() * (MAX_VALUE - MIN_VALUE) + MIN_VALUE);
      valueControl.setValue(randomNum);
      expect(value$.getValue()).toBe(randomNum);
    }
  });

  it(`should value be equal to ${MIN_VALUE}`, () => {
    valueControl.setValue(1);
    expect(value$.getValue()).toBe(MIN_VALUE);
  });

  it(`should value be equal to ${MIN_VALUE}`, () => {
    valueControl.setValue(-42);
    expect(value$.getValue()).toBe(MIN_VALUE);
  });

  it(`should value be equal to ${MAX_VALUE + 500}`, () => {
    valueControl.setValue(MAX_VALUE + 500);
    expect(value$.getValue()).toBe(MAX_VALUE);
  });

  it(`should value be equal to ${MAX_VALUE + 25}`, () => {
    valueControl.setValue(MAX_VALUE + 25);
    expect(value$.getValue()).toBe(MAX_VALUE);
  });

});
