import { Component, input } from '@angular/core';
import { ImprovActivity } from '@app/shared/model/ImprovActivity';

@Component({
  selector: 'app-activity-card',
  imports: [],
  templateUrl: './activity-card.html',
  styleUrl: './activity-card.scss',
})
export class ActivityCard {
  activity = input<ImprovActivity>();

}
