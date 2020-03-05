class Solution(object):
    def addTwoNumbers(self, l1, l2):
         root = ListNode(0) # create a root node, the return result will be the number behind this node
        result = root # let the result bound with rood node
        carry = 0 # create a carry for reference
        while l1 or l2 or carry == 1: # if l1, l2 or carry is exist
            value = 0 # create a empty value
            if l1: # if l1 exist, then sign the l1 value to empty value, and move the l1 to next one
                value += l1.val
                l1 = l1.next
            if l2: # if l2 exist, then sign the l2 value to empty value, and move the l2 to next one
                value += l2.val
                l2 = l2.next
            value += carry # add the final value to carry to calculate current value
            root.next = ListNode(value % 10) # take ones digit from the result
            carry = int(value / 10) # get carry
            root = root.next # root move to next
        return result.next # return to nest node (first always zero)

#Create test case & environment
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def initList(array):
    root = ListNode(array[0])
    result = root
    for index, value in enumerate(array):
        if index > 0:
            root.next = ListNode(value)
            root = root.next
    return result

def printList(linkList):
    if linkList:
        print("[", end="")
        while linkList.next:
            print(linkList.val, end=", ")
            linkList = linkList.next
        print(linkList.val, end="]\n")
    else:
        print("[]")

def execute():
    l1 = initList([2, 3, 4])
    l2 = initList([3, 5, 7])
    sol = Solution()
    printList(sol.addTwoNumbers(l1, l2))

if __name__ == "__main__":
    execute()
