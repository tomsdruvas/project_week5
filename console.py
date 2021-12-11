import pdb

from models.workout import Workout
from models.activity import Activity
from models.member import Member

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


# activity_repository.delete_all()
# workout_repository.delete_all()
# member_repository.delete_all()


# member1 = Member("John", 20, "Premium", True)
# member2 = Member("Paul", 25, "Standard", True)
# workout1 = Workout("HIIT", 10)
# workout2 = Workout("Cardio", 12)
# member_repository.save(member1)
# member_repository.save(member2)
# workout_repository.save(workout1)
# workout_repository.save(workout2)


# results = member_repository.select_all()
# for member in results:
#     print(member.__dict__)

# results = workout_repository.select_all()
# for workout in results:
#     print(workout.__dict__)



# activity1 = Activity(workout1, member1)
# activity2 = Activity(workout2, member2)

# activity_repository.save(activity1)
# activity_repository.save(activity2)


# results = activity_repository.select_all()
# for activity in results:
#     print(activity)



# member3 = Member("Duncan", 23, "Standard", True)
# member_repository.save(member3)

member_repository.delete(17)