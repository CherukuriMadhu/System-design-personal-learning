Definition

The Observer Pattern establishes a one-to-many relationship where:

When one object changes state, all dependent objects are automatically notified.

Think:

Observer = Subscribe and notify

Real-world example

YouTube channel.

YouTube Channel
      ↓
New Video
      ↓
Notify subscribers
 ↓       ↓       ↓
User A  User B  User C

The channel doesn't need to manually know what each subscriber does.

Before Observer ❌
class YouTubeChannel:

    def upload_video(self):
        print("New video uploaded")

        user1.notify()
        user2.notify()
        user3.notify()

Problem:

The channel directly depends on users.

Adding/removing subscribers requires changing the channel code.

After Observer ✅
class Subscriber:

    def update(self, video):
        print("New video:", video)

Subject:

class YouTubeChannel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def upload_video(self, video):

        print("Uploaded:", video)

        for subscriber in self.subscribers:
            subscriber.update(video)

Usage:

channel = YouTubeChannel()

user1 = Subscriber()
user2 = Subscriber()

channel.subscribe(user1)
channel.subscribe(user2)

channel.upload_video("Python Design Patterns")

Output:

Uploaded: Python Design Patterns
New video: Python Design Patterns
New video: Python Design Patterns
Structure
             Subject
                |
        ┌───────┼───────┐
        ↓       ↓       ↓
    Observer Observer Observer
Real-world examples
YouTube subscribers
News subscriptions
Event systems
GUI event listeners
Stock price notifications
Interview definition

Observer Pattern defines a one-to-many dependency so that when the subject changes state, all registered observers are automatically notified.