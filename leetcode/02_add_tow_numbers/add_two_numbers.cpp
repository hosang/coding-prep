/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(-1);
        ListNode* p = &head;
        int carry = 0;
        while(l1 != NULL || l2 != NULL) {
            int sum = carry;
            if(l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;
            }
            carry = sum / 10;
            p->next = new ListNode(sum % 10);
            p = p->next;
        }
        if(carry > 0) {
            p->next = new ListNode(carry);
        }
        return head.next;
    }
};
