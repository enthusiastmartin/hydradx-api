from dataclasses import dataclass
from typing import Optional, List

from hydradxapi.pallets import Pallet


@dataclass
class Vote:
    referendum_id: int
    amount: int


@dataclass
class PositionVote:
    position_id: int
    votes: List[Vote]


class Staking(Pallet):
    MODULE_NAME = "Staking"

    def position_votes(self) -> [PositionVote]:
        entries = self.query_entries(self.MODULE_NAME, "PositionVotes")
        result = []
        for entry in entries:
            position_id = int(entry[0].value)
            vote_entries = entry[1].value.copy()
            votes = []
            for vote_entry in vote_entries["votes"]:
                ref_id = vote_entry[0]
                amount = vote_entry[1]["amount"]
                votes.append(Vote(ref_id, amount))
            if len(votes) > 0:
                result.append(PositionVote(position_id, votes))
        return result
