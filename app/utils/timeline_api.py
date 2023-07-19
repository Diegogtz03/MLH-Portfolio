from playhouse.shortcuts import model_to_dict

def get_posts(TimelinePost):
  return {
    'timeline_posts': [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
  }