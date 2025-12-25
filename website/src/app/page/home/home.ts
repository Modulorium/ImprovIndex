import { Component } from '@angular/core';

import { ImprovActivityExample } from '@app/shared/model/ImprovActivityExample';
import { ActivityCard } from "@app/shared/component/activity-card/activity-card";

@Component({
  selector: 'app-home',
  imports: [ActivityCard],
  templateUrl: './home.html',
  styleUrls: ['./home.scss'],
})
export class Home {
  activityExample = ImprovActivityExample.getExample();
}
