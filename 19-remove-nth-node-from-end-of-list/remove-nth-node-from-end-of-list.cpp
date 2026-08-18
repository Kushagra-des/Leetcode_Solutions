class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode* slow = &dummy;
        ListNode* fast = &dummy;

        // Move fast n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            fast = fast->next;
        }

        // Move both pointers
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // Remove nth node from end
        slow->next = slow->next->next;

        return dummy.next;
    }
};