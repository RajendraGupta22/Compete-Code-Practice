package org.example;
//https://github.com/RajendraGupta22/Compete-Code-Practice/blob/main/LAZY%20INTERN%20JAVA%20PROBLEM.docx


import java.util.*;
 class Node{
    private int row;
    private int col;
    private Character elm;

     public Node(int row, int col, Character elm) {
         this.row = row;
         this.col = col;
         this.elm = elm;
     }

     public int getRow() {
         return row;
     }

     public void setRow(int row) {
         this.row = row;
     }

     public int getCol() {
         return col;
     }

     public void setCol(int col) {
         this.col = col;
     }

     public Character getElm() {
         return elm;
     }

     public void setElm(Character elm) {
         this.elm = elm;
     }

     @Override
     public String toString() {
         return "Node{" +
                 "row=" + row +
                 ", col=" + col +
                 ", elm=" + elm +
                 '}';
     }
 }
public class Main {
    static List<String> generateTestInput(){
       return Arrays.asList(
                "OOOO OOOM",
                "OOVO OOOO",
                "OVOO OOVO",
                "OOOO OOOO",
                "OOOO OOOO",
                "OOOO OOOO",
                "OOOO VOOO",
                "OVOO OOOO"
        );
    }
    public static void main(String[] args) {
//        List<String> data = generateInput();
        List<String> data = generateTestInput();
        int nRow = data.size();
        Map nodeResult = computeNodes(data);
        List<Node> vacant = (List<Node>) nodeResult.get("vacant");
        List<Node> manager = (List<Node>) nodeResult.get("manager");
        Float floatPositiveInf = Float.POSITIVE_INFINITY;
        List SmallestNode = new ArrayList<>();
        for (Node source : vacant) {
            int dist = findShortDist( source, manager.get(0) );
            if( dist < floatPositiveInf ){
                floatPositiveInf = (float) dist;
                if(SmallestNode.size()>0){
                    SmallestNode.set(0, source.toString() );
                }else{
                    SmallestNode.add( source.toString() );
                }
            }
        }
        if(SmallestNode.size()>0){
            System.out.println(" dist : "+floatPositiveInf);
            System.out.println(" node is : "+SmallestNode);
        }else{
            System.out.println(0);
        }
    }

    static int findShortDist( Node startNode, Node endNode){
        int extra_space = 0;
        int row_space = Math.abs( endNode.getRow() - startNode.getRow() );
        List<Integer> firstSection = Arrays.asList(0,1,2,3);
        List<Integer> secondSection =  Arrays.asList(5,6,7,8);
        if( firstSection.contains(startNode.getCol()) && firstSection.contains(endNode.getCol()) ){
            // do nothing
        } else if( secondSection.contains(startNode.getCol()) && secondSection.contains(endNode.getCol()) ){
            // do nothing
        }else{
            extra_space = 2;
        }
        return extra_space+row_space;
    }
    static List<String> generateInput(){
        System.out.println("Hello world!");
        Scanner sc = new Scanner(System.in);
        int nRow = Integer.parseInt(sc.nextLine());
        List<String> data = new ArrayList<String>();
        for(int i=0;i<nRow;i++){ data.add( sc.nextLine() ); }
        display(data);
        return data;
    }
     static void display(List<String> data) {
        for (int i = 0; i < data.size(); i++) {
            System.out.println( data.get(i) );
        }
    }
    static Map computeNodes(List<String> data){
        Map result = new HashMap();
        List<Node> visited = new ArrayList<Node>();
        List<Node> manager = new ArrayList<Node>();
        for (int row=0;row<data.size();row++) {
            String item = data.get(row);
            for(int col=0;col<item.length();col++ ){
                Character sub = item.charAt(col);
                if(sub.equals('V')){
                    visited.add(new Node(row,col,sub) );
                } else if (sub.equals('M')) {
                    manager.add(new Node(row,col,sub));
                }
            }
        }
        result.put("vacant",visited);
        result.put("manager",manager);
        return result;
    }
}
