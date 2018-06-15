package test;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import seg.APSeg;
import seg.CWS;
import seg.MMSeg;

public class Demo {
	public static void main(String[] args) {

		String modelFile = "./data/model/model1_pku.txt";
		modelFile = "./data/model/model1+pku.txt";
		CWS cws = new CWS();
		cws.weights.loadModel(modelFile);
		MMSeg.Init();
		String testLine;
		//  Ϊ�����ʵ��
		//  �о�������Դ
		//  ���ĺ���δ������
		//  ������������
		//  �����Ӧ��Ӣ����������ͨ��
		//	������ķȥ�����¡�
		//	����ͷ��ʾͬ���ҵ������
		//	���Ǽ����԰���Ķ�־ӭ���µ�һ�ꡣ
		//	����ר��ѧ��40���˲μ����ֻᡣ
		System.out.println("�����������䣺");
		Scanner in=new Scanner(System.in);
		while(!(testLine = in.nextLine()).equals("end")) {
			ArrayList<String> mmRes= MMSeg.segment(testLine);
			
			ArrayList<String> apRes = APSeg.segment(cws, testLine);
			System.out.println("���˫��ƥ��ִʽ��:");
			System.out.println(mmRes);
			System.out.println("ƽ����֪���ִʽ��");
			System.out.println(apRes);
			System.out.println("�����������䣺");
		}
	}
}
