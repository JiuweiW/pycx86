import cparse
from cvisitors import Visitor

class Liveness(Visitor):
    def __init__(self):
        Visitor.__init__(self)
    
    def vTranslationUnit(self, node):
        print "Translation Unit"
        self._visitList(node.nodes)
    
    def vFunctionDefn(self, node):
        print "Function Definition"
        node.body.accept(self)
    
    def vCompoundStatement(self, node):
        print "Compound Statement"
        node.statement_list.accept(self)
        
    def vNodeList(self, node):
        print "Node List"
        self._visitList(node.nodes)
        
    def vIfStatement(self, node):
        print "If"
        
    def vWhileLoop(self, node):
        print "While"
        
    def vForLoop(self, node):
        print "For"
        
    def vBreakStatement(self, node):
        print "Break"
        
    def vContinueStatement(self, node):
        print "Continue"
        
    def vStringLiteral(self, node):
        print "String"
        
    def vConst(self, node):
        print "Const"
        
    def vId(self, node):
        print "Id"
        
    def vArrayExpression(self, node):
        print "Array"
        
    def vFunctionExpression(self, node):
        print "Function Call"
        
    def vReturnStatement(self, node):
        print "Return"
        
    def vBinop(self, node):
        print "Binop"
        
    def vNegative(self, node):
        print "Negative"
        
    def vPointer(self, node):
        print "Pointer"
        
    def vAddrOf(self, node):
        print "Addr Of"