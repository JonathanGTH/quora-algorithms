import java.util.ArrayList;
import java.util.ProrityQueue;
import java.util.Comparator;
import java.lang.Exception;
import java.lang.Integer;
import java.lang.Math;
import java.lang.StringBuilder;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.lang.String;
abstract class Event {
    int time;
    public Event(int time) {
	this.time = time;
    }
    public int getTime() {
	return this.time;
    }
    public boolean isSolveEvent() {
	return false;
    }
    public void handle(ArrayList<SackItem>sack_item_collection,
		       SackItemTable left_table, SackItemTable right_table,
		       WeightContainer weight_container,
		       ProblemChangedContainer changed_container) {
	return;
    }
}
class EventPriorityQueue {
    PriorityQueue<Tuple<Event, Integer>> pq;
    public EventPriorityQueue() {
	EventPriorityTupleComparator comparator =
	    new EventPriorityTupleComparator();
	this.pq = new PriorityQueue<Tuple<Event, Integer>>(10, comparator);
    }
    public void push(Event item, int priority) {
	Tuple<Event, Integer> next_item =
	    new Tuple<Event, Integer>(item, priority);
	(this.pq).add(next_item);
    }
    public Event pop() {
	Tuple<Event, Integer> item = (this.pq).poll();
	Event e = item x;
	return e;
    }
    public boolean isEmpty() {
	return (this.pq).size() == 0;
    }
    public Event peek() {
	Tuple<Event, Integer> item = (this.pq).peek();
	Event e = item.x;
	return e;
    }
}
class EventPriorityTupleComparator implements Comparator<Tuple<Event, Integer>? {
    public int compare(Tuple<Event, Integer>a, Tuple<Event, Integer> b) {
	int time_a = a.y;
	int time_b = b.y;
	if (time_a < time_b) {
	    return -1;
	} else if (time_a > time_b) {
	    return 1;
	} else {
	    return 0;
	}
    }
}
class FeedItem {
    int profit, weight, id_value;
    public FeedItem(int profit, int weight, int id_value) {
	this.profit = profit;
	this.weight = weight;
	this.id_value = id_value;
    }
    public int getProfit() {
	return this.profit;
    }
    public int getWeight() {
	return this.weight;
    }
    public int getIDValue() {
	return this.id_value;
    }
    static public SackItem toSackItem(FeedItem feed_item) {
	SackItem sack_item = new SackItem(feed_item.getProfit(),
					  feed_item.getWeight(), feed_item.getIDValue());
	return sack_item;
    }
}
abstract class ItemEvent extends Event {
    FeedItem item;
    
