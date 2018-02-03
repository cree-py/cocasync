# WarlogItem

## Variables
| Variable | Description | Type |
|----------|-------------|------|
| state | The current state of the war. | String |
| teamSize | The amount of people on each team. | Integer |
| preparationStartTime | When the preparation started. | String |
| startTime | When the war started. | String |
| endTime | When the war ended. | String |

## Methods
| Method | Description | Returns |
|--------|-------------|---------|
| getHomeClan() | Returns the home clan. | [Clan](https://github.com/cree-py/cocasync/blob/master/documentation/CLAN.md) |
| getOpponentClan() | Returns the visitor clan. | [Clan](https://github.com/cree-py/cocasync/blob/master/documentation/CLAN.md) |