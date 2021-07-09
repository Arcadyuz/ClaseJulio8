import java.util.Scanner;
public class HolaT {
	public static void main(String[] args){
		var sc = new Scanner(System.in);
		System.out.print("Digite su nombre: ");
		var nombre = sc.nextLine();
		System.out.println("Hola " + nombre + " !");
	}
	
}
